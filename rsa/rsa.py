import rsa

txt = bytes(input("Input: "), 'utf-8')

(PublicKey, PrivateKey) = rsa.newkeys(512)


encrypt = rsa.encrypt(txt, PublicKey)
print(f'Encrypt : {encrypt}')

decrypt = rsa.decrypt(encrypt, PrivateKey)
print(f'Decrypt : {decrypt}')
