PYTHON_INTERPRETER=python3
AUTH_FP=auth.json

help:
	@echo "Use \`make <target>\` where \`<target>\` is one of"
	@echo "  init   initialize friends"

init:
	@$(PYTHON_INTERPRETER) scripts/init_friends_ids.py "$(AUTH_FP)" \
		> data/friends_ids.json
