import frida, sys

flog = open('frida_test.log', 'w')

def on_message(message, data):
	global flog
	if message['type'] == 'send':
		print("[*] {0}".format(message['payload']))
		flog.write("[*] {0}".format(message['payload']))
	else:
		print(message)

def get_agent_source() -> str:
	import os, codecs
	agent_path = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), '_agent.js'))
	if not os.path.exists(agent_path):
		raise Exception('Unable to locate agent sources at: {0}.'.format(agent_path))

	with codecs.open(agent_path, 'r', 'utf-8') as f:
		source = f.read()

	return source


def inner_cb(data):
	print(data)

device = frida.get_usb_device()
# pid = device.spawn(['com.google.android.calendar'])
pid = device.spawn(['com.android.chrome'])
session = device.attach(pid)
script = session.create_script(get_agent_source())
script.on('message', on_message)
script.load()
script.exports.hook_class_method('android.app.ContextImpl', 'uncaughtException')
device.resume(pid)
sys.stdin.read()
