import config as _config

supabase = _config.supabase
SUPABASE_JWT_SECRET = getattr(_config, 'SUPABASE_JWT_SECRET', None)
