#!/usr/bin/python3
"""__init__ method for directory modela"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
