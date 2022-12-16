import qrcode
meuqr = qrcode.make("https://youtu.be/rEnD32kbw6I")
type(meuqr)
meuqr.save("QR.png")