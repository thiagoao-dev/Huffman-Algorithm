import json

class FileClass:

    @staticmethod
    def readJson(filePath):
        try:
            with open(filePath) as json_file:
                file = json.load(json_file)
                assert isinstance(file, object)
                return file
        except IOError as err:
            return "Arquivo nao encontrado"

    @staticmethod
    def readTxt(filePath):
        try:
            with open(filePath) as txt_file:
                file = txt_file.read()
                assert isinstance(file, object)
                return file
        except IOError as err:
            return "Arquivo nao encontrado"

    @staticmethod
    def getChars(filePath):
        #
        if filePath.find(".json") >= 0:
            # Ordena do maior para o menor peso
            list = sorted(
                FileClass.readJson(filePath)['tree']['nodes'],
                key=lambda chars: chars[2], reverse=True
            )
            #
            return list
        #
        elif filePath.find(".txt") >= 0:

            list   = []
            readed = []
            txt = FileClass.readTxt(filePath)

            # Lista caracter por caracter
            for i in range(len(txt)):
                # Atribui o caracter não visitado a lista
                if txt[i] not in readed:
                    readed.append(txt[i])
                    list.append([txt[i],1,0])
                else:
                    for item in list:
                        if item[0] == txt[i]:
                            item[1] += 1
            # Calcula o peso
            for item in list:
                item[2] = round( # Arredonda o número
                    (
                        (
                            (item[1]*100) / len(txt)
                        ) / 100
                    ),
                    3 # Total de casas apos a virgula
                )
            # Ordena do maior para o menor peso
            list = sorted(
                list,
                key=lambda chars: chars[2], reverse=True
            )
            #
            return list

print(FileClass.getChars("texto.txt"))
print(FileClass.getChars("texto-descomp.json"))