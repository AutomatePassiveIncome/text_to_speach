from mateco import TTS
mod = TTS()
mod.setup_voice('am')
mod.convert("hi, how are you")
mod.speak()
mod.close()

