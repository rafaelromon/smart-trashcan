import blescan
import sys
import time

import bluetooth._bluetooth as bluez


def getPeso():
    dev_id = 0

    sock = bluez.hci_open_dev(dev_id)

    blescan.hci_le_set_scan_parameters(sock)
    blescan.hci_enable_le_scan(sock)

    measured_anterior = 0

    salir = False
    try:
        while True:
            returnedList = blescan.parse_events(sock, 1)
            if len(returnedList) > 0:

                for p in returnedList:
                    (mac, uuid, major, minor, txpower, rssi) = p.split(',', 6)
                    # CAMBIAR LA DIRECCION MAC

                    if mac == "c8:0f:10:c1:bc:9a":
                    
                        measunit = uuid[22:24]
                        measured = int((uuid[26:28] + uuid[24:26]), 16) * 0.01

                        unit = 'kg'

                        if measunit.startswith(('03', 'b3')):
                            unit = 'lbs'
                        if measunit.startswith(('12', 'b2')):
                            unit = 'jin'
                        if measunit.startswith(('22', 'a2')):
                            unit = 'kg'  # measured = measured / 2
                        if unit:
                            # print("measured : %s %s" % (measured/2, unit))
                            return str(measured/2) + unit
    except KeyboardInterrupt:
        sys.exit(1)


if __name__ == "__main__":
    print(getPeso())

