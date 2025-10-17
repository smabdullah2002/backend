import sys
import importlib

# Shim package to allow imports like `from app.config import ...`
# Map app submodule names to existing top-level modules in this folder.
try:
    config_mod = importlib.import_module('config')
    sys.modules.setdefault('app.config', config_mod)
except Exception:
    pass

try:
    auth_mod = importlib.import_module('auth')
    sys.modules.setdefault('app.auth', auth_mod)
except Exception:
    pass

try:
    blog_mod = importlib.import_module('blog')
    sys.modules.setdefault('app.blog', blog_mod)
except Exception:
    pass

__all__ = ['config', 'auth', 'blog']
