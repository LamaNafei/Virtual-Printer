from flask import Flask, jsonify, render_template, request
from printer import Printer


app = Flask(__name__)
printer = Printer()
doc = ""
@app.route('/', methods=['POST', 'GET'])
def printerSetting() :
    global printer
    return render_template('printer.html', key = printer.status.name)


# Printer status
@app.route('/status', methods=['GET'])
def get_status():
    global printer
    return jsonify({'status': printer.status.name,
                    'last run': printer.lastRun,
                    'print count': printer.printCount,
                    'last print': printer.lastPrint})

# Print
@app.route('/print', methods=['POST'])
def post_print():
    global printer, doc
    doc = request.files["doc"].filename
    if doc is None or doc == "":
        return jsonify({'error': 'no document was selected'})
    json = printer.collect_doc(doc)
    return jsonify(json)

# Cancel Print
@app.route('/cancel', methods=['POST'])
def post_cancel():
    global printer
    json = printer.cancel_print()
    return jsonify(json)

# Pause Print
@app.route('/pause', methods=['POST'])
def post_pause():
    global printer
    printer.pause_print()
    return jsonify({'status': printer.status.name})

# Resume Print
@app.route('/resume', methods=['POST'])
def post_resume():
    global printer
    printer.resume_print()
    return jsonify({'status': printer.status.name})

# Check Ink or Toner Levels
@app.route('/levels', methods=['GET'])
def get_levels():
    global printer
    return jsonify({"ink level": printer.check_levels})


if __name__ == '__main__':
    app.run(debug = True)
