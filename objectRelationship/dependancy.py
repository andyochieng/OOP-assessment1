class Printer:
    def print_document(self, document):
        print(f"Printing: {document.content}")

class Document:
    def __init__(self, content):
        self.content = content


document = Document("Hello World")
printer=Printer()
printer.print_document(document)