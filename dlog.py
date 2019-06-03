# This is a generated file! Please edit source .ksy file and use kaitai-struct-compiler to rebuild

from pkg_resources import parse_version
from kaitaistruct import __version__ as ks_version, KaitaiStruct, KaitaiStream, BytesIO
from enum import Enum


if parse_version(ks_version) < parse_version('0.7'):
    raise Exception("Incompatible Kaitai Struct Python API: 0.7 or later is required, but you have %s" % (ks_version))

class Dlog(KaitaiStruct):

    class DlogFormats(Enum):
        openscope = 1
        openlogger = 3

    class StopReasons(Enum):
        normal = 0
        forced = 1
        error = 2
        overflow = 3
        unknown = 4
    def __init__(self, _io, _parent=None, _root=None):
        self._io = _io
        self._parent = _parent
        self._root = _root if _root else self
        self._read()

    def _read(self):
        self.endianness = self._io.read_u1()
        self.body = self._root.Body(self._io, self, self._root)

    class Body(KaitaiStruct):
        def __init__(self, _io, _parent=None, _root=None):
            self._io = _io
            self._parent = _parent
            self._root = _root if _root else self
            self._read()

        def _read(self):
            _on = self._root.endianness
            if _on == 0:
                self._is_le = True
            elif _on == 1:
                self._is_le = False

            if self._is_le == True:
                self._read_le()
            elif self._is_le == False:
                self._read_be()
            else:
                raise Exception("Unable to decide endianness")

        def _read_le(self):
            self.header = self._root.Body.Header(self._io, self, self._root, self._is_le)

        def _read_be(self):
            self.header = self._root.Body.Header(self._io, self, self._root, self._is_le)

        class Header(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):

                if self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()
                else:
                    raise Exception("Unable to decide endianness")

            def _read_le(self):
                self.sample_size = self._io.read_u1()
                self.header_size = self._io.read_u2le()
                self.start_of_data = self._io.read_u2le()
                self.dlog_format = KaitaiStream.resolve_enum(self._root.DlogFormats, self._io.read_u2le())
                self.dlog_version = self._io.read_u4le()
                self.voltage_scale = self._io.read_u8le()
                self.stop_reason = KaitaiStream.resolve_enum(self._root.StopReasons, self._io.read_u4le())
                self.sample_initial_index = self._io.read_u8le()
                self.num_samples = self._io.read_u8le()
                self.sample_rate_scale = self._io.read_u8le()
                self.raw_sample_rate = self._io.read_u8le()
                self.delay_scale = self._io.read_u8le()
                self.raw_delay = self._io.read_s8le()
                if self.dlog_format == self._root.DlogFormats.openlogger:
                    self.num_openlogger_channels = self._io.read_u4le()

                if self.dlog_format == self._root.DlogFormats.openlogger:
                    self.openlogger_channel_map = [None] * (8)
                    for i in range(8):
                        self.openlogger_channel_map[i] = self._io.read_u1()



            def _read_be(self):
                self.sample_size = self._io.read_u1()
                self.header_size = self._io.read_u2be()
                self.start_of_data = self._io.read_u2be()
                self.dlog_format = KaitaiStream.resolve_enum(self._root.DlogFormats, self._io.read_u2be())
                self.dlog_version = self._io.read_u4be()
                self.voltage_scale = self._io.read_u8be()
                self.stop_reason = KaitaiStream.resolve_enum(self._root.StopReasons, self._io.read_u4be())
                self.sample_initial_index = self._io.read_u8be()
                self.num_samples = self._io.read_u8be()
                self.sample_rate_scale = self._io.read_u8be()
                self.raw_sample_rate = self._io.read_u8be()
                self.delay_scale = self._io.read_u8be()
                self.raw_delay = self._io.read_s8be()
                if self.dlog_format == self._root.DlogFormats.openlogger:
                    self.num_openlogger_channels = self._io.read_u4be()

                if self.dlog_format == self._root.DlogFormats.openlogger:
                    self.openlogger_channel_map = [None] * (8)
                    for i in range(8):
                        self.openlogger_channel_map[i] = self._io.read_u1()



            @property
            def sample_rate(self):
                if hasattr(self, '_m_sample_rate'):
                    return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None

                self._m_sample_rate = ((1.0 * self.raw_sample_rate) / self.sample_rate_scale)
                return self._m_sample_rate if hasattr(self, '_m_sample_rate') else None

            @property
            def delay(self):
                if hasattr(self, '_m_delay'):
                    return self._m_delay if hasattr(self, '_m_delay') else None

                self._m_delay = ((1.0 * self.raw_delay) / self.delay_scale)
                return self._m_delay if hasattr(self, '_m_delay') else None

            @property
            def num_channels(self):
                if hasattr(self, '_m_num_channels'):
                    return self._m_num_channels if hasattr(self, '_m_num_channels') else None

                self._m_num_channels = (self.num_openlogger_channels if self.dlog_format == self._root.DlogFormats.openlogger else 1)
                return self._m_num_channels if hasattr(self, '_m_num_channels') else None

            @property
            def channel_map(self):
                if hasattr(self, '_m_channel_map'):
                    return self._m_channel_map if hasattr(self, '_m_channel_map') else None

                self._m_channel_map = (self.openlogger_channel_map if self.dlog_format == self._root.DlogFormats.openlogger else [0])
                return self._m_channel_map if hasattr(self, '_m_channel_map') else None


        class Data(KaitaiStruct):
            def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                self._io = _io
                self._parent = _parent
                self._root = _root if _root else self
                self._is_le = _is_le
                self._read()

            def _read(self):

                if self._is_le == True:
                    self._read_le()
                elif self._is_le == False:
                    self._read_be()
                else:
                    raise Exception("Unable to decide endianness")

            def _read_le(self):
                self.samples = []
                i = 0
                while not self._io.is_eof():
                    self.samples.append(self._root.Body.Data.Sample(self._io, self, self._root, self._is_le))
                    i += 1


            def _read_be(self):
                self.samples = []
                i = 0
                while not self._io.is_eof():
                    self.samples.append(self._root.Body.Data.Sample(self._io, self, self._root, self._is_le))
                    i += 1


            class Sample(KaitaiStruct):
                def __init__(self, _io, _parent=None, _root=None, _is_le=None):
                    self._io = _io
                    self._parent = _parent
                    self._root = _root if _root else self
                    self._is_le = _is_le
                    self._read()

                def _read(self):

                    if self._is_le == True:
                        self._read_le()
                    elif self._is_le == False:
                        self._read_be()
                    else:
                        raise Exception("Unable to decide endianness")

                def _read_le(self):
                    self.channel = [None] * (self._root.body.header.num_channels)
                    for i in range(self._root.body.header.num_channels):
                        _on = self._root.body.header.sample_size
                        if _on == 1:
                            self.channel[i] = self._io.read_s1()
                        elif _on == 2:
                            self.channel[i] = self._io.read_s2le()
                        elif _on == 4:
                            self.channel[i] = self._io.read_s4le()


                def _read_be(self):
                    self.channel = [None] * (self._root.body.header.num_channels)
                    for i in range(self._root.body.header.num_channels):
                        _on = self._root.body.header.sample_size
                        if _on == 1:
                            self.channel[i] = self._io.read_s1()
                        elif _on == 2:
                            self.channel[i] = self._io.read_s2be()
                        elif _on == 4:
                            self.channel[i] = self._io.read_s4be()




        @property
        def data(self):
            if hasattr(self, '_m_data'):
                return self._m_data if hasattr(self, '_m_data') else None

            _pos = self._io.pos()
            self._io.seek(self.header.start_of_data)
            if self._is_le:
                self._m_data = self._root.Body.Data(self._io, self, self._root, self._is_le)
            else:
                self._m_data = self._root.Body.Data(self._io, self, self._root, self._is_le)
            self._io.seek(_pos)
            return self._m_data if hasattr(self, '_m_data') else None



