# ERRORS FUNCTIONS #
def error(msg: str, errtype: str) -> None:
	print (f"SecPi {errtype} error: {msg}")

def panic(msg: str, errtype: str, code: int) -> None:
	error(msg, errtype)
	raise SystemExit(code)
