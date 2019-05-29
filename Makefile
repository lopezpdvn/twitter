PYTHON_INTERPRETER=python3
AUTH_FP=_data/auth.json

help:
	@echo "Use \`make <target>\` where \`<target>\` is one of"
	@echo "  init             initialize friends"
	@echo "  retrieve-friends retrieve friends"
	@echo "  take-random      take n random friends, default n = 10"

init:
	@$(PYTHON_INTERPRETER) scripts/init_friends_ids.py "$(AUTH_FP)" \
		> _data/friends_ids.json

retrieve-friends:
	@$(PYTHON_INTERPRETER) scripts/retrieve_friends.py \
		--auth-filepath _data/auth.json \
		_data/friends_ids.json

take-random:
	@$(PYTHON_INTERPRETER) scripts/select_random.py
