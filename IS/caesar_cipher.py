def encrypt(key,message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    message = message.upper()
    for i in message:
        enc_ind = (alpha.index(i)+key)%len(alpha)
        result +=alpha[enc_ind]
    return result






def decrypt(key,message):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    message = message.upper()
    for i in message:
        dec_ind = (alpha.index(i)-key)%len(alpha)
        result +=alpha[dec_ind]
    return result



print(encrypt(3,"Harshil"))
print(decrypt(3,encrypt(3,"Harshil")))