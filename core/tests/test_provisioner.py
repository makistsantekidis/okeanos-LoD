import mock

from fokia.provisioner import Provisioner

test_flavors = [{u'SNF:allow_create': True,
                 u'SNF:disk_template': u'drbd',
                 u'SNF:volume_type': 1,
                 u'disk': 20,
                 u'id': 1,
                 u'links': [{u'href': u'https://cyclades.okeanos.grnet.gr/compute/v2.0/flavors/1',
                             u'rel': u'self'},
                            {u'href': u'https://cyclades.okeanos.grnet.gr/compute/v2.0/flavors/1',
                             u'rel': u'bookmark'}],
                 u'name': u'C1R1024D20drbd',
                 u'ram': 1024,
                 u'vcpus': 1},
                {u'SNF:allow_create': True,
                 u'SNF:disk_template': u'drbd',
                 u'SNF:volume_type': 1,
                 u'disk': 40,
                 u'id': 3,
                 u'links': [{u'href': u'https://cyclades.okeanos.grnet.gr/compute/v2.0/flavors/3',
                             u'rel': u'self'},
                            {u'href': u'https://cyclades.okeanos.grnet.gr/compute/v2.0/flavors/3',
                             u'rel': u'bookmark'}],
                 u'name': u'C1R1024D40drbd',
                 u'ram': 1024,
                 u'vcpus': 1},
                {u'SNF:allow_create': True,
                 u'SNF:disk_template': u'drbd',
                 u'SNF:volume_type': 1,
                 u'disk': 20,
                 u'id': 4,
                 u'links': [{u'href': u'https://cyclades.okeanos.grnet.gr/compute/v2.0/flavors/4',
                             u'rel': u'self'},
                            {u'href': u'https://cyclades.okeanos.grnet.gr/compute/v2.0/flavors/4',
                             u'rel': u'bookmark'}],
                 u'name': u'C1R2048D20drbd',
                 u'ram': 2048,
                 u'vcpus': 1}]

test_images = [{u'created': u'2015-06-26T11:29:59+00:00',
                u'id': u'0035ac89-a86e-4108-93e8-93e294b74a3d',
                u'is_snapshot': False,
                u'links': [{
                    u'href': u'https://cyclades.okeanos.grnet.gr/compute/v2.0/images/0035ac89-a86e-4108-93e8-93e294b74a3d',
                    u'rel': u'self'},
                    {
                        u'href': u'https://cyclades.okeanos.grnet.gr/compute/v2.0/images/0035ac89-a86e-4108-93e8-93e294b74a3d',
                        u'rel': u'bookmark'},
                    {
                        u'href': u'https://cyclades.okeanos.grnet.gr/image/v1.0/images/0035ac89-a86e-4108-93e8-93e294b74a3d',
                        u'rel': u'alternate'}],
                u'metadata': {
                    u'description': u'ArchLinux 2015.06.26 with openssh and iptables setup - accepting only PubKeyAuth',
                    u'gui': u'No GUI',
                    u'kernel': u'4.0.6-1',
                    u'os': u'archlinux',
                    u'osfamily': u'linux',
                    u'partition_table': u'gpt',
                    u'root_partition': u'1',
                    u'sortorder': u'7400000',
                    u'users': u'root'},
                u'name': u'archlinux-2015.06.26',
                u'progress': 100,
                u'public': True,
                u'status': u'ACTIVE',
                u'tenant_id': u'7e271a0b-1427-45ec-9916-f8e72bfbf3d4',
                u'updated': u'2015-06-26T11:29:59+00:00',
                u'user_id': u'7e271a0b-1427-45ec-9916-f8e72bfbf3d4'},
               {u'created': u'2014-03-11T12:55:07+00:00',
                u'id': u'0099593e-4f6d-48bf-8f03-0cec7fabb05b',
                u'is_snapshot': False,
                u'links': [{
                    u'href': u'https://cyclades.okeanos.grnet.gr/compute/v2.0/images/0099593e-4f6d-48bf-8f03-0cec7fabb05b',
                    u'rel': u'self'},
                    {
                        u'href': u'https://cyclades.okeanos.grnet.gr/compute/v2.0/images/0099593e-4f6d-48bf-8f03-0cec7fabb05b',
                        u'rel': u'bookmark'},
                    {
                        u'href': u'https://cyclades.okeanos.grnet.gr/image/v1.0/images/0099593e-4f6d-48bf-8f03-0cec7fabb05b',
                        u'rel': u'alternate'}],
                u'metadata': {u'description': u'Master clone',
                              u'os': u'ubuntu',
                              u'osfamily': u'linux',
                              u'partition_table': u'msdos',
                              u'root_partition': u'1',
                              u'users': u'user hduser'},
                u'name': u'master_clone',
                u'progress': 100,
                u'public': True,
                u'status': u'ACTIVE',
                u'tenant_id': u'607bc20e-ae01-46ca-8a7d-d37b92e9908f',
                u'updated': u'2014-03-11T12:55:07+00:00',
                u'user_id': u'607bc20e-ae01-46ca-8a7d-d37b92e9908f'}]

test_projects = [{u'creation_date': u'2015-06-09T09:46:44.327826+00:00',
                  u'description': u'',
                  u'end_date': u'2015-11-30T00:00:00+00:00',
                  u'homepage': u'',
                  u'id': u'6ff62e8e-0ce9-41f7-ad99-13a18ecada5f',
                  u'join_policy': u'moderated',
                  u'leave_policy': u'auto',
                  u'max_members': 9223372036854775807,
                  u'name': u'lambda.grnet.gr',
                  u'owner': u'69c6686c-4e3e-407e-96b4-c21ef7d5def5',
                  u'private': False,
                  u'resources': {u'astakos.pending_app': {u'member_capacity': 0,
                                                          u'project_capacity': 0},
                                 u'cyclades.cpu': {u'member_capacity': 80,
                                                   u'project_capacity': 80},
                                 u'cyclades.disk': {u'member_capacity': 1073741824000,
                                                    u'project_capacity': 1073741824000},
                                 u'cyclades.floating_ip': {u'member_capacity': 10,
                                                           u'project_capacity': 10},
                                 u'cyclades.network.private': {u'member_capacity': 5,
                                                               u'project_capacity': 5},
                                 u'cyclades.ram': {u'member_capacity': 128849018880,
                                                   u'project_capacity': 128849018880},
                                 u'cyclades.vm': {u'member_capacity': 20,
                                                  u'project_capacity': 20},
                                 u'pithos.diskspace': {u'member_capacity': 0,
                                                       u'project_capacity': 0}},
                  u'state': u'active',
                  u'system_project': False}]

test_quotas = { '6ff62e8e-0ce9-41f7-ad99-13a18ecada5f':
             {'cyclades.disk':
                  {'project_limit': 1288490188800, 'project_pending': 0, 'project_usage': 64424509440, 'usage': 0, 'limit': 322122547200, 'pending': 0},
              'cyclades.vm':
                  {'project_limit': 60, 'project_pending': 0, 'project_usage': 2, 'usage': 0, 'limit': 15, 'pending': 0},
              'pithos.diskspace':
                  {'project_limit': 429496729600, 'project_pending': 0, 'project_usage': 0, 'usage': 0, 'limit': 107374182400, 'pending': 0},
              'cyclades.ram':
                  {'project_limit': 128849018880, 'project_pending': 0, 'project_usage': 12884901888, 'usage': 0, 'limit': 32212254720, 'pending': 0},
              'cyclades.cpu':
                  {'project_limit': 120, 'project_pending': 0, 'project_usage': 12, 'usage': 0, 'limit': 30, 'pending': 0},
              'cyclades.floating_ip':
                  {'project_limit': 10, 'project_pending': 0, 'project_usage': 6, 'usage': 3, 'limit': 4, 'pending': 0},
              'cyclades.network.private':
                  {'project_limit': 10, 'project_pending': 0, 'project_usage': 7, 'usage': 0, 'limit': 4, 'pending': 0},
              'astakos.pending_app':
                  {'project_limit': 0, 'project_pending': 0, 'project_usage': 0, 'usage': 0, 'limit': 0, 'pending': 0}} }

def test_find_flavor():
    with mock.patch('fokia.provisioner.astakos'), \
         mock.patch('fokia.provisioner.KamakiConfig'), \
         mock.patch('fokia.provisioner.cyclades'):
        provisioner = Provisioner("lambda")
        provisioner.astakos.get_projects.return_value = test_projects
        provisioner.cyclades.list_images.return_value = test_images
        provisioner.cyclades.list_flavors.return_value = test_flavors

        provisioner.create_vm(vm_name="tost", project_name="lambda.grnet.gr",
                              project_mode="supahpower", image_name="archlinux")
        provisioner.cyclades.create_server.assert_called_with(
            name='tost', image_id=u'0035ac89-a86e-4108-93e8-93e294b74a3d', flavor_id=3,
            project_id=u'6ff62e8e-0ce9-41f7-ad99-13a18ecada5f', networks=[], personality=[])

def test_check_all_resources():
    with mock.patch('fokia.provisioner.astakos'), \
         mock.patch('fokia.provisioner.KamakiConfig'), \
         mock.patch('fokia.provisioner.cyclades'):
        provisioner = Provisioner("lambda")
        provisioner.astakos.get_projects.return_value = test_projects
        provisioner.astakos.get_quotas.return_value = test_quotas
        provisioner.check_all_resources(test_quotas,  project_id=u'6ff62e8e-0ce9-41f7-ad99-13a18ecada5f',
                                                      slaves=2,
                                                      cluster_size=3,
                                                      vcpus=12,
                                                      ram=4096*3,
                                                      disk=180,
                                                      ip_request=1,
                                                      network_request=1)

if __name__ == "__main__":
    test_find_flavor()
