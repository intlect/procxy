from flask import Flask, send_file, request, render_template

app = Flask(__name__)


@app.route('/')
def home():
    urls = {
        'nanom - lin' : '/nanom?param=lin',
        'lolm - lin' : '/lolm?param=lin',
        'rigel - lin' : '/rigel?param=lin',
        'gmnr - lin' : '/gmnr?param=lin',
        'nanom - win' : '/nanom?param=win',
        'lolm - win' : '/lolm?param=win',
        'gmnr - win' : '/gmnr?param=win',
    }
    return render_template('home.html', urls=urls)


@app.route('/nanom')
def nanom():
    param =  request.args.get('os')
    if param == "lin":
        return send_file('bin_files/nanom', as_attachment=True)
    if param == "win":
        return send_file('bin_files/nanom.exe', as_attachment=True)
    else:
        return send_file('bin_files/nanom', as_attachment=True)

@app.route('/lolm')
def lolm():
    param =  request.args.get('os')
    if param == "lin":
        return send_file('bin_files/lolm', as_attachment=True)
    if param == "win":
        return send_file('bin_files/lolm.exe', as_attachment=True)
    else:
        return send_file('bin_files/lolm', as_attachment=True)

@app.route('/rigel')
def rigel():
    param =  request.args.get('os')
    if param == "lin":
        return send_file('bin_files/rigel', as_attachment=True)
    else:
        return send_file('bin_files/rigel', as_attachment=True)

@app.route('/gmnr')
def gmnr():
    param =  request.args.get('os')
    if param == "lin":
        return send_file('bin_files/gmnr', as_attachment=True)
    if param == "win":
        return send_file('bin_files/gmnr.exe', as_attachment=True)
    else:
        return send_file('bin_files/gmnr', as_attachment=True)

if __name__ == '__main__':
    app.run()
