import sys
import collections.abc

sys.modules['collections.Mapping'] = collections.abc.Mapping
sys.modules['collections.MutableMapping'] = collections.abc.MutableMapping
