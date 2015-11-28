from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
	return render_template('Research_Question.html')

@app.route('/about')
def about():
	return render_template('About_the_Author.html')

@app.route('/methodology')
def methodology():
	return render_template('Methodology.html')

@app.route('/projectdescription')
def project_description():
	return render_template('Project_Description.html')

@app.route('/results')
def results():
	return render_template('Results.html')

if __name__ == '__main__':
    app.run()  



	