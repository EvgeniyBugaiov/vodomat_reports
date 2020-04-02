from apps.settings import config
import os

def test_o_folders_existss():
    assert os.path.exists(config['o']['source']), 'Folder O Source does not exists'
    assert os.path.exists(config['o']['destination']), 'Folder O Destination does not exists'


def test_z_folders_exitsts():
    assert os.path.exists(config['z']['source']), 'Folder Z Source does not exists'
    assert os.path.exists(config['z']['destination']), 'Folder Z Destination does not exists'


def test_r_folders_exitsts():
    assert os.path.exists(config['r']['source']), 'Folder R Source does not exists'
    assert os.path.exists(config['r']['destination']), 'Folder R Destination does not exists'


def test_archive_folders_exists():
    assert os.path.exists(os.path.join(config['o']['destination'], config['archive'])), 'Folder O Archive does not exists'
    assert os.path.exists(os.path.join(config['z']['destination'], config['archive'])), 'Folder Z Archive does not exists'
    assert os.path.exists(os.path.join(config['r']['destination'], config['archive'])), 'Folder R Archive does not exists'
