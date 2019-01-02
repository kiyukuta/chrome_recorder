export ENV_NAME=venv
export BASE_DIR=`dirname $0`
export VIRTUALENV_PATH=${BASE_DIR}/${ENV_NAME}
export PYTHON=$VIRTUALENV_PATH/bin/python

mkdir -p ${BASE_DIR}/result
${PYTHON} ${BASE_DIR}/record.py --blacklist ${BASE_DIR}/blacklist.txt  2> ${BASE_DIR}/error.txt
