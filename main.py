from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)


@app.route('/upload')
def upload_file():
    return render_template('index.html')


@app.route('/uploader', methods=['GET', 'POST'])
def uploader():
    if request.method == 'POST':
        f = request.files['file']
        f.save('uploads/uploaded_script.m')

        output = subprocess.run(['matlab', '-nodisplay', '-nodesktop', '-nojvm', '-nosplash', '-r',
                                 '"try, run(\'uploads/uploaded_script.m\'), catch, exit, end, exit"', '-logfile',
                                 'log.txt'],
                                check=True, stdout=subprocess.PIPE, universal_newlines=True)

        return output.stdout


if __name__ == "__main__":
    app.run(debug=True)
