from configs import transforms_config


DATASETS = {
	'ffhq_encode': {
		'transforms': transforms_config.EncodeTransforms,
		'train_source_root': 'datasets/EG3D_FFHQ/final_crops',
		'train_target_root': 'datasets/EG3D/final_crops',
		'test_source_root': 'datasets/EG3D_CelebA/final_crops',
		'test_target_root':'datasets/EG3D_CelebA/final_crops',
	}
}
