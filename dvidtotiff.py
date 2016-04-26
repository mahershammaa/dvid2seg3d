from libdvid import DVIDNodeService
import numpy as np
from tifffile import *
import code

server_address = 'http://104.196.106.27:8000/'
uuid = '0d3d16fa990f41a9b6d4b322e5631c65'
node_service = DVIDNodeService(server_address, uuid)

instance_name = 'VCN_c13_bin5_EM.nrrd'
#node_service.create_keyvalue(keyvalue_store)

data = node_service.get_gray3D(instance_name, (512,512,512), (0,0,0))

imsave(instance_name + '.tif', data)

image = imread(instance_name + '.tif')
np.testing.assert_array_equal(image,data)

with TiffFile(instance_name + '.tif') as tif:
	images = tif.asarray()
	for page in tif:
		for tag in page.tags.values():
			t = tag.name, tag.value
		image = page.asarray()

code.interact(local=locals())