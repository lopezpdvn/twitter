PYTHON_INTERPRETER=python3
AUTH_FP=_data/auth.json

help:
	@echo "Use \`make <target>\` where \`<target>\` is one of"
	@echo "  init             initialize friends"
	@echo "  retrieve-friends retrieve friends"

init:
	@$(PYTHON_INTERPRETER) scripts/init_friends_ids.py "$(AUTH_FP)" \
		> _data/friends_ids.json

retrieve-friends:
	@$(PYTHON_INTERPRETER) scripts/retrieve_friends.py \
		_data/friends_ids.json
