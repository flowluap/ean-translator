import sys
import time

NULL_CHAR = chr(0)
chars = {
'ALT-t':chr(4)+NULL_CHAR*2 +chr(23)+NULL_CHAR*5,
'A':chr(2)+NULL_CHAR+chr(4)+NULL_CHAR*5,
'B':chr(2)+NULL_CHAR+chr(5)+NULL_CHAR*5,
'C':chr(2)+NULL_CHAR+chr(6)+NULL_CHAR*5,
'D':chr(2)+NULL_CHAR+chr(7)+NULL_CHAR*5,
'E':chr(2)+NULL_CHAR+chr(8)+NULL_CHAR*5,
'F':chr(2)+NULL_CHAR+chr(9)+NULL_CHAR*5,
'G':chr(2)+NULL_CHAR+chr(10)+NULL_CHAR*5,
'H':chr(2)+NULL_CHAR+chr(11)+NULL_CHAR*5,
'I':chr(2)+NULL_CHAR+chr(12)+NULL_CHAR*5,
'J':chr(2)+NULL_CHAR+chr(13)+NULL_CHAR*5,
'K':chr(2)+NULL_CHAR+chr(14)+NULL_CHAR*5,
'L':chr(2)+NULL_CHAR+chr(15)+NULL_CHAR*5,
'M':chr(2)+NULL_CHAR+chr(16)+NULL_CHAR*5,
'N':chr(2)+NULL_CHAR+chr(17)+NULL_CHAR*5,
'O':chr(2)+NULL_CHAR+chr(18)+NULL_CHAR*5,
'P':chr(2)+NULL_CHAR+chr(19)+NULL_CHAR*5,
'Q':chr(2)+NULL_CHAR+chr(20)+NULL_CHAR*5,
'R':chr(2)+NULL_CHAR+chr(21)+NULL_CHAR*5,
'S':chr(2)+NULL_CHAR+chr(22)+NULL_CHAR*5,
'T':chr(2)+NULL_CHAR+chr(23)+NULL_CHAR*5,
't':NULL_CHAR*2 +chr(23)+NULL_CHAR*5,
'U':chr(2)+NULL_CHAR+chr(24)+NULL_CHAR*5,
'V':chr(2)+NULL_CHAR+chr(25)+NULL_CHAR*5,
'W':chr(2)+NULL_CHAR+chr(26)+NULL_CHAR*5,
'X':chr(2)+NULL_CHAR+chr(27)+NULL_CHAR*5,
'Y':chr(2)+NULL_CHAR+chr(28)+NULL_CHAR*5,
'Z':chr(2)+NULL_CHAR+chr(29)+NULL_CHAR*5,
'1':NULL_CHAR*2 +chr(30)+NULL_CHAR*5,
'2':NULL_CHAR*2 +chr(31)+NULL_CHAR*5,
'3':NULL_CHAR*2 +chr(32)+NULL_CHAR*5,
'4':NULL_CHAR*2 +chr(33)+NULL_CHAR*5,
'5':NULL_CHAR*2 +chr(34)+NULL_CHAR*5,
'6':NULL_CHAR*2 +chr(35)+NULL_CHAR*5,
'7':NULL_CHAR*2 +chr(36)+NULL_CHAR*5,
'8':NULL_CHAR*2 +chr(37)+NULL_CHAR*5,
'9':NULL_CHAR*2 +chr(38)+NULL_CHAR*5,
'0':NULL_CHAR*2 +chr(39)+NULL_CHAR*5,
'!':chr(2)+NULL_CHAR+chr(30)+NULL_CHAR*5,
'@':chr(2)+NULL_CHAR+chr(31)+NULL_CHAR*5,
'#':chr(2)+NULL_CHAR+chr(32)+NULL_CHAR*5,
'&':chr(2)+NULL_CHAR+chr(36)+NULL_CHAR*5,
'*':chr(2)+NULL_CHAR+chr(37)+NULL_CHAR*5,
'(':chr(2)+NULL_CHAR+chr(38)+NULL_CHAR*5,
')':chr(2)+NULL_CHAR+chr(39)+NULL_CHAR*5,
'-':NULL_CHAR*2 +chr(45)+NULL_CHAR*5,
'=':NULL_CHAR*2 +chr(46)+NULL_CHAR*5,
'{':NULL_CHAR*2 +chr(47)+NULL_CHAR*5,
'}':NULL_CHAR*2 +chr(48)+NULL_CHAR*5,
'\\':NULL_CHAR*2 +chr(49)+NULL_CHAR*5,
';':NULL_CHAR*2 +chr(51)+NULL_CHAR*5,
'':NULL_CHAR*2 +chr(52)+NULL_CHAR*5,
'`':NULL_CHAR*2 +chr(53)+NULL_CHAR*5,
',':NULL_CHAR*2 +chr(54)+NULL_CHAR*5,
'.':NULL_CHAR*2 +chr(55)+NULL_CHAR*5,
'/':NULL_CHAR*2 +chr(56)+NULL_CHAR*5,
':':chr(2)+NULL_CHAR+chr(51)+NULL_CHAR*5,
'"':chr(2)+NULL_CHAR+chr(52)+NULL_CHAR*5,
'<':chr(2)+NULL_CHAR+chr(54)+NULL_CHAR*5,
'>':chr(2)+NULL_CHAR+chr(55)+NULL_CHAR*5,
'?':chr(2)+NULL_CHAR+chr(56)+NULL_CHAR*5,
'}':NULL_CHAR*2 +chr(79)+NULL_CHAR*5,
'{':NULL_CHAR*2 +chr(80)+NULL_CHAR*5,
']':chr(2)+NULL_CHAR+chr(79)+NULL_CHAR*5,
'[':chr(2)+NULL_CHAR+chr(80)+NULL_CHAR*5,
' ':NULL_CHAR*2+chr(44)+NULL_CHAR*5,
'~':chr(2)+NULL_CHAR+chr(53)+NULL_CHAR*5,
'_':chr(2)+NULL_CHAR+chr(45)+NULL_CHAR*5,
'$':chr(2)+NULL_CHAR+chr(33)+NULL_CHAR*5,
'/':NULL_CHAR*2 +chr(56)+NULL_CHAR*5,
'+':chr(2)+NULL_CHAR+chr(46)+NULL_CHAR*5,
'%':chr(2)+NULL_CHAR+chr(34)+NULL_CHAR*5,
    }

hid = { 4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'f', 10: 'g', 11: 'h', 12: 'i', 13: 'j', 14: 'k', 15: 'l', 16: 'm', 17: 'n', 18: 'o', 19: 'p', 20: 'q', 21: 'r', 22: 's', 23: 't', 24: 'u', 25: 'v', 26: 'w', 27: 'x', 28: 'y', 29: 'z', 30: '1', 31: '2', 32: '3', 33: '4', 34: '5', 35: '6', 36: '7', 37: '8', 38: '9', 39: '0', 44: ' ', 45: '-', 46: '=', 47: '[', 48: ']', 49: '\\', 51: ';' , 52: '\'', 53: '~', 54: ',', 55: '.', 56: '/'  }

hid2 = { 4: 'A', 5: 'B', 6: 'C', 7: 'D', 8: 'E', 9: 'F', 10: 'G', 11: 'H', 12: 'I', 13: 'J', 14: 'K', 15: 'L', 16: 'M', 17: 'N', 18: 'O', 19: 'P', 20: 'Q', 21: 'R', 22: 'S', 23: 'T', 24: 'U', 25: 'V', 26: 'W', 27: 'X', 28: 'Y', 29: 'Z', 30: '!', 31: '@', 32: '#', 33: '$', 34: '%', 35: '^', 36: '&', 37: '*', 38: '(', 39: ')', 44: ' ', 45: '_', 46: '+', 47: '{', 48: '}', 49: '|', 51: ':' , 52: '"', 53: '~', 54: '<', 55: '>', 56: '?'  }

fp = open('/dev/hidraw0', 'rb')

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

ss = ""
shift = False


while True:
    ## Get the character from the HID
    buffer = fp.read(8)
    for c in buffer:
        if ord(c) > 0:
            ##  40 is carriage return which signifies
            ##  we are done looking for characters
            if int(ord(c)) == 40:
                print ss
                print ss[7:12]
                if ss[:7] == "2100000":
                    write_report(chars["ALT-t"])
                    write_report(NULL_CHAR*8)
                    time.sleep(0.8)
                    ss = ss[7:12]
                    for char in ss:
                        if char in chars.keys(): 
                            write_report(chars[char])            
                            write_report(NULL_CHAR*8)
                        else:
                                write_report(chars["*"])            

	            write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)
		    write_report(NULL_CHAR*8)
                else:
                    for char in ss:
                            write_report(NULL_CHAR*8)
                            if char in chars.keys(): 
                                write_report(chars[char])            
                            else:
                                write_report(chars["*"])            
                            
	            write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)
		    write_report(NULL_CHAR*8)
		ss = ""
		break;
            ##  If we are shifted then we have to 
            ##  use the hid2 characters.
            if shift: 
                ## If it is a '2' then it is the shift key
                if int(ord(c)) == 2 :
                    shift = True
                ## if not a 2 then lookup the mapping
                else:
                    ss += hid2[ int(ord(c)) ]
                    shift = False
            ##  If we are not shifted then use
            ##  the hid characters
            else:
                ## If it is a '2' then it is the shift key
                if int(ord(c)) == 2 :
                    shift = True
                ## if not a 2 then lookup the mapping
                else:
                    ss += hid[ int(ord(c)) ]
