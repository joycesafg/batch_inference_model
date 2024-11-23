# batch-inference documentation!

## Description

A pipeline for batch inference with automatic retrain

## Commands

The Makefile contains the central entry points for common tasks related to this project.

### Syncing data to cloud storage

* `make sync_data_up` will use `az storage blob upload-batch -d` to recursively sync files in `data/` up to `batch-inference/data/`.
* `make sync_data_down` will use `az storage blob upload-batch -d` to recursively sync files from `batch-inference/data/` to `data/`.


