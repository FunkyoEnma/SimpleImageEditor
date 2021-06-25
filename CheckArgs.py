# Check in the args for the mandatory and optional args
import os

import App
import Errors


class CheckArgsv:

    def __init__(self, argsv: list[str]):
        """
        This class is going to check in all the given args if the mandatory an optional args was given
        :param argsv: List of args (you may givwe sys.argsv)
        """
        self.__args = argsv
        self.__argsDir = dict()

        # Check for the Mandatory arg InputImage
        igiven, value, iarg = self.__checkArg(App.Args.InputImage)

        if igiven:
            del igiven

            if value is None:
                Errors.Parameters.noValue(iarg)
            elif not os.path.exists(value):
                Errors.Parameters.notExist(value)
            elif not os.path.splitext(value)[1].replace(".", "") in App.validFormats:
                Errors.Parameters.notValidFileType(os.path.splitext(value)[1].replace(".", ""))
        else:
            Errors.Parameters.noArg(App.Args.InputImage)

        self.__argsDir[App.Args.InputImage] = value

    def __checkArg(self, arg: App.Args):
        """
        Check if the given arg is in the app execute args
        :param arg: Desired arg, it may be an Enum from App.Args.<DesiredArg>.name
        :return: Retuns a boolean an optionaly an string, True + Str(value) if arg found, False if arg not found
        """

        _arg = None

        for i in self.__args:
            _arg, value = self.__argAndData(i)
            if _arg in App.avaibleArgs[arg]:
                return True, value, _arg

        return False, None, _arg

    def __argAndData(self, i0: str):
        arg = i0.split("=")[0].replace("-", "")

        try:
            value = i0.split("=")[1]
        except IndexError:
            value = None

        return arg, value

    def getArg(self, arg: App.Args):
        try:
            return self.__argsDir[arg]
        except KeyError:
            return App.defaultArgs[arg]

    @property
    def ImageInput(self):
        return self.getArg(App.Args.InputImage)

    @property
    def EnableRounded(self):
        return self.getArg(App.Args.EnableRounded)

    @property
    def args(self):
        return self.__args
