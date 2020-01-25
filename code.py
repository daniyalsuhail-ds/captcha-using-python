# Install python Library captcha
# pip install captcha

from captcha.audio import AudioCaptcha
from captcha.image import ImageCaptcha


# put font name in parameters if you need
image = ImageCaptcha()

# Data of Captcha Image
data = image.generate('1234')

# 1.png is file name
image.write('1234', '1.png')

# For audio captcha

# put font name in parameters if you need
audio = AudioCaptcha()

# Data of Captcha Audio
# 123.wav is audio file
data = audio.generate('50932')
audio.write('50932', '123.wav')
