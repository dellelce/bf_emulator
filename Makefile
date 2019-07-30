# Use for standard activities
all:
	@echo 'Use "tests" the original(+continue) and "jests" for code using dictionary/json'

tests:
	@python -c 'import tests; tests.test_all();' && echo "Success"

jests:
	@python -c 'import jests; jests.test_all();' && echo "Success"
