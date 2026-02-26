import unittest

from pycycling.heart_rate_service import _parse_hr_measurement, HeartRateMeasurement


class TestHeartRateServiceService(unittest.TestCase):
    def test__parse_csc_measurement(self):
        self.assertEqual(_parse_hr_measurement(
            bytearray([
                0b00000000,  # flags
                0b00101010,  # bpm
            ])),
            HeartRateMeasurement(
                sensor_contact=None,
                bpm=42,
                rr_interval=[],
                energy_expended=None
            )
        )
        self.assertEqual(_parse_hr_measurement(
            bytearray([
                0b00000100,  # flags
                0b00101010,  # bpm
            ])),
            HeartRateMeasurement(
                sensor_contact=False,
                bpm=42,
                rr_interval=[],
                energy_expended=None
            )
        )
        self.assertEqual(_parse_hr_measurement(
            bytearray([
                0b00000110,  # flags
                0b00101010,  # bpm
            ])),
            HeartRateMeasurement(
                sensor_contact=True,
                bpm=42,
                rr_interval=[],
                energy_expended=None
            )
        )
        self.assertEqual(_parse_hr_measurement(
            bytearray([
                0b00000001,  # flags
                0b00101010,  # bpm LSO
                0b00000001,  # bpm MSO
            ])),
            HeartRateMeasurement(
                sensor_contact=None,
                bpm=298,
                rr_interval=[],
                energy_expended=None
            )
        )
        self.assertEqual(_parse_hr_measurement(
            bytearray([
                0b00001000,  # flags
                0b00101010,  # bpm
                0b11101000,  # energy_expended LSO
                0b00000011,  # energy_expended MSO
            ])),
            HeartRateMeasurement(
                sensor_contact=None,
                bpm=42,
                rr_interval=[],
                energy_expended=1000
            )
        )
        self.assertEqual(_parse_hr_measurement(
            bytearray([
                0b00010000,  # flags
                0b00101010,  # bpm
                0b00100000,  # rr_interval[0] LSO
                0b00000011,  # rr_interval[0] MSO
            ])),
            HeartRateMeasurement(
                sensor_contact=None,
                bpm=42,
                rr_interval=[800],
                energy_expended=None
            )
        )
        self.assertEqual(_parse_hr_measurement(
            bytearray([
                0b00011101,  # flags
                0b00101010,  # bpm LSO
                0b00000001,  # bpm MSO
                0b11101000,  # energy_expended LSO
                0b00000011,  # energy_expended MSO
                0b00100000,  # rr_interval[0] LSO
                0b00000011,  # rr_interval[0] MSO
                0b01011000,  # rr_interval[1] LSO
                0b00000010,  # rr_interval[1] MSO
            ])),
            HeartRateMeasurement(
                sensor_contact=False,
                bpm=298,
                rr_interval=[800, 600],
                energy_expended=1000
            )
        )


if __name__ == '__main__':
    unittest.main()
