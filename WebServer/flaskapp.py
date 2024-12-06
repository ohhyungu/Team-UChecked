from flask import Flask, render_template, redirect, url_for, request, session, flash
import paho.mqtt.client as mqtt

users = {'22011755':'22011755'}
broker_url = '127.0.0.1'

app = Flask(__name__)
app.secret_key = 'ABABAB234wdfeweasdfewwq'

def check_login():
	if 'logged_in' not in session:
		return False
	return True

def mqtt_subscribe(userid):
	mqtt_client = mqtt.Client()
	mqtt_client.connect(broker_url, 1883)
	mqtt_client.loop_start()

	topic_name = topic_str # 2ë²
	message = message_str
	mqtt_client.publish(topic = topic_name, payload = message)
	mqtt_client.loop_stop()

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']

		if username in users and password == users[username]:
			session['userid'] = username
			session['logged_in'] = True
			return redirect(url_for('mainpage'))
		else:
			return redirect(url_for('login'))
			flash('login fail')

	return render_template('login.html')

@app.route('/mainpage')
def mainpage():
	if not check_login():
		return redirect(url_for('login'))
	try:
		userid = session['userid']
	except:
		return redirect(url_for('login'))

	return render_template('index.html')

@app.route('/daeyangai')
def daeyangai():
	return render_template('daeyangai.html')

@app.route('/')
def index():
	session.clear()

	return redirect(url_for('login'))

if __name__ == '__main__':
	app.run(dhost='127.0.0.1', port=8765, debug=True)
