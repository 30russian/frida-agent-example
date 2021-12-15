### How to compile & load

```sh
$ git clone https://github.com/30russian/frida-agent-example.git
$ cd frida-agent-example/
$ npm install
$ virtualenv ./venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ npm run build
run emulator
$ adb root
$ adb push frida-server-15.1.14-android-x86_64 /data/local/tmp/
$ adb shell "chmod 755 /data/local/tmp/frida-server-15.1.14-android-x86_64"
$ adb shell "/data/local/tmp/frida-server-15.1.14-android-x86_64 &"
$ python frida_test_locally.py
```

### Development workflow

To continuously recompile on change, keep this running in a terminal:

```sh
$ npm run watch
```

And use an editor like Visual Studio Code for code completion and instant
type-checking feedback.
