# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from trajecgenerator/plotTrajecXoYRequest.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class plotTrajecXoYRequest(genpy.Message):
  _md5sum = "af80c98d097b90c478c238e3c9f71a07"
  _type = "trajecgenerator/plotTrajecXoYRequest"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """string title
uint8 typeXoY   # 0 für x, 1 für y
float32 maxT
float32 dT
float32 k
float32[2] xrange
float32[2] yrange
"""
  __slots__ = ['title','typeXoY','maxT','dT','k','xrange','yrange']
  _slot_types = ['string','uint8','float32','float32','float32','float32[2]','float32[2]']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       title,typeXoY,maxT,dT,k,xrange,yrange

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(plotTrajecXoYRequest, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.title is None:
        self.title = ''
      if self.typeXoY is None:
        self.typeXoY = 0
      if self.maxT is None:
        self.maxT = 0.
      if self.dT is None:
        self.dT = 0.
      if self.k is None:
        self.k = 0.
      if self.xrange is None:
        self.xrange = [0.] * 2
      if self.yrange is None:
        self.yrange = [0.] * 2
    else:
      self.title = ''
      self.typeXoY = 0
      self.maxT = 0.
      self.dT = 0.
      self.k = 0.
      self.xrange = [0.] * 2
      self.yrange = [0.] * 2

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self.title
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B3f().pack(_x.typeXoY, _x.maxT, _x.dT, _x.k))
      buff.write(_get_struct_2f().pack(*self.xrange))
      buff.write(_get_struct_2f().pack(*self.yrange))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.title = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.title = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.typeXoY, _x.maxT, _x.dT, _x.k,) = _get_struct_B3f().unpack(str[start:end])
      start = end
      end += 8
      self.xrange = _get_struct_2f().unpack(str[start:end])
      start = end
      end += 8
      self.yrange = _get_struct_2f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self.title
      length = len(_x)
      if python3 or type(_x) == unicode:
        _x = _x.encode('utf-8')
        length = len(_x)
      buff.write(struct.Struct('<I%ss'%length).pack(length, _x))
      _x = self
      buff.write(_get_struct_B3f().pack(_x.typeXoY, _x.maxT, _x.dT, _x.k))
      buff.write(self.xrange.tostring())
      buff.write(self.yrange.tostring())
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      start = end
      end += 4
      (length,) = _struct_I.unpack(str[start:end])
      start = end
      end += length
      if python3:
        self.title = str[start:end].decode('utf-8', 'rosmsg')
      else:
        self.title = str[start:end]
      _x = self
      start = end
      end += 13
      (_x.typeXoY, _x.maxT, _x.dT, _x.k,) = _get_struct_B3f().unpack(str[start:end])
      start = end
      end += 8
      self.xrange = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
      start = end
      end += 8
      self.yrange = numpy.frombuffer(str[start:end], dtype=numpy.float32, count=2)
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_2f = None
def _get_struct_2f():
    global _struct_2f
    if _struct_2f is None:
        _struct_2f = struct.Struct("<2f")
    return _struct_2f
_struct_B3f = None
def _get_struct_B3f():
    global _struct_B3f
    if _struct_B3f is None:
        _struct_B3f = struct.Struct("<B3f")
    return _struct_B3f
# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from trajecgenerator/plotTrajecXoYResponse.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class plotTrajecXoYResponse(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "trajecgenerator/plotTrajecXoYResponse"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(plotTrajecXoYResponse, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    if python3:
      codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
class plotTrajecXoY(object):
  _type          = 'trajecgenerator/plotTrajecXoY'
  _md5sum = 'af80c98d097b90c478c238e3c9f71a07'
  _request_class  = plotTrajecXoYRequest
  _response_class = plotTrajecXoYResponse
