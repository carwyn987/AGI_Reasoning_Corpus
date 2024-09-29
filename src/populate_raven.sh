################# Generate dataset ##################################

export RAVEN_NUM_SAMPLES=1
export RAVEN_DATA_DIR=$RAVEN_BASE/data

if [ ! -d "$RAVEN_DATA_DIR" ]; then
  mkdir $RAVEN_DATA_DIR
fi

cd $RAVEN_BASE/src
python -m dataset.main --num-samples $RAVEN_NUM_SAMPLES --save-dir $RAVEN_DATA_DIR
cd $BASE_DIR