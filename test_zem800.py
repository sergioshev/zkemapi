from  zkemapi import zkem
import pprint



fichero=zkem()
fichero.connect(host = '192.168.1.36', debug = True)
#fichero.get_attendance_log()
#fichero.clear_attendance_log()
#log = fichero.unpack_attendance_log()
#pprint.pprint(log)
#f = open('salida.bin', 'wb')
#f.write("".join(fichero._zkem__logdata))
#f.close()
ts = fichero.get_time()
pprint.pprint(ts)
fichero.disconnect()
