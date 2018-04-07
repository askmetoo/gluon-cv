"""Utility functions."""
from __future__ import absolute_import

from .download import download
from .filesystem import makedirs
from .bbox import bbox_iou
from .block import set_lr_mult

from .lr_scheduler import PolyLRScheduler
from .metrics.voc_segmentation import batch_pix_accuracy, batch_intersection_union
from .parallel import ModelDataParallel, CriterionDataParallel
