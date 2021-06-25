import App


class Parameters:

    @staticmethod
    def noArg(arg: App.Args):
        raise AttributeError("Args Error", f"You may give the {arg.name} with one of this parameters:"
                                           f"{App.avaibleArgs[App.Args.InputImage]}")

    @staticmethod
    def noValue(arg: App.Args):
        raise AttributeError("Arg Data Error", f"The parameter '{arg}' may have a valid image path")

    @staticmethod
    def notValidFileType(i0):
        raise TypeError("File type not valid", f"The file extension ({i0}) is not a valid one, please use one of these "
                                               f"instead: {App.validFormats}")

    @staticmethod
    def notExist(file):
        raise FileNotFoundError(f"File not fund at: \"{file}\", please verify")
