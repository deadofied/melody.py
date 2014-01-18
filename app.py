from flask import Flask, render_template
from melody import *
import random

class MyFlask(Flask):
    def get_send_file_max_age(self, name):
        if name.lower().endswith('.mp3'):
            return 1
        return 60

app = MyFlask(__name__)

@app.route("/")
def hello():
	total_time_elapsed = 0.0
	success = False
	while not success:
		success, results = generate_melody(False)
		if results:
			lower_voice, upper_voice, key_signature, time_elapsed, tries = results
			total_time_elapsed += time_elapsed
	print lower_voice
	print upper_voice
	return render_template('play_midi.html', 
		lowerVoice=lower_voice, 
		upperVoice=upper_voice, 
		keySignature=key_signature,
		rand=random.randint(1, 99999),
		timeElapsed=total_time_elapsed
	)

if __name__ == "__main__":
	app.debug = True
	app.run()