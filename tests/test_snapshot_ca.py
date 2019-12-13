import unittest
import logging,time

logging.basicConfig(level=logging.DEBUG)

from snapshot.ca_core.snapshot_ca import Snapshot


class TestSnapshotReqFile(unittest.TestCase):

    def tearDown(self):
        pass

    def test_load(self):
        #snapshot = Snapshot("testfiles/SF_settings.req")
        snapshot = Snapshot("/sf/data/applications/snapshot/req/op/SF_settings.req")
        # request_file = SnapshotReqFile("testfiles/SF_timing.req")
        # pvs = request_file.read()

        print()
        # print(pvs)

        for i in range(10):
            print(snapshot.get_disconnected_pvs_names())
            print("# disconnected: %d" % len(snapshot.get_disconnected_pvs_names()))
            print("# connected: %d" % (len(snapshot.pvs) - len(snapshot.get_disconnected_pvs_names())))
            print(len(snapshot.pvs))
            print()
            time.sleep(1)

        snapshot.clear_pvs()
        # logging.info(len(pvs))

if __name__ == '__main__':
    unittest.main()
