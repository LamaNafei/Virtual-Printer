import datetime
from printerStatus import PrinterStatus


class Printer:
    def __init__(self):
        
        self.status = PrinterStatus.Idle
        self.queue = []
        self.lastPrint = None
        self.lastRun = None
        self.printCount = 0
        self.paused = True


    def print_document(self, document):

        self.status = PrinterStatus.Printing
        while len(self.queue) > 0 and self.paused :
            print(self.queue.pop())
        if self.paused :
            self.printCount = self.printCount + 1
            self.status = PrinterStatus.Idle
        self.lastPrint = document
        self.lastRun = datetime.datetime.now().strftime("%H:%M:%S")
        return {'status': self.status.name,
                'Print Count': self.printCount,
                'Last Run:': self.lastRun,
                'last print': self.lastPrint}
    
    
    def collect_doc(self, document) :
        
        if self.status == PrinterStatus.Printing :
            self.queue.append(document)
            self.status = PrinterStatus.Busy
            return {"status": self.status.name,}
        if self.status != PrinterStatus.Idle :
            self.status = PrinterStatus.Error
            return {"error": "printer is busy",
                    "status" : self.status.name}
        self.queue.append(document)
        return self.print_document(document)

    def cancel_print(self):

        if self.status != PrinterStatus.Printing :
            return {'error': 'printer is not printing to cancel it'}
        self.queue.clear()
        self.printCount = self.printCount - 1
        self.status = PrinterStatus.Cancelled
        return {'status': self.status.name}

    def pause_print(self):       
        self.status = PrinterStatus.Paused
        self.paused = False


    def resume_print(self):

        self.status = PrinterStatus.Printing
        self.paused = True
        self.print_document

# I cannot get how to develop without real Printer
    def check_levels(self):

        ...

# I cannot get how to develop without real Printer
    def replace_cartridges(self):
        ...


    def calibrate_printer(self):

        self.status = PrinterStatus.Idle


    def power_on(self):

        self.status = PrinterStatus.Idle


    def power_off(self):

        self.status = PrinterStatus.Offline


# I cannot get how to develop without real Printer
    def update_firmware(self):
        ...


    def reset_printer(self):

        self.queue.clear
