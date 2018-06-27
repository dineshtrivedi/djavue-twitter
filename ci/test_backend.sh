#!/bin/bash
docker-compose -f docker/compose/test.yml run djavue-twitter unittests.sh
exitcode=$?
docker-compose -f docker/compose/test.yml down
exit $exitcode
