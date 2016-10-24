{
	'targets': [ 
	{
		'target_name': 'new64',
		'type': 'executable',
		'msbuild_toolset': '<!(echo %TOOLSET%)',

		'msbuild_configuration_attributes': {
			'CharacterSet': '2',
			'IntermediateDirectory': '$(Configuration)/$(ProjectName)/',
		},
		
		 'include_dirs': [
          '../includes/',
		  '../src/'
        ],
		
		'default_configuration': 'Debug',
		'conditions': [	
			['library_type == "static_library"', {
				'defines':[
					
				],
			}],
			['OS == "win"', {
				'defines':[
					'_CRT_SECURE_NO_WARNINGS',
					'_SCL_SECURE_NO_WARNINGS',
					'WIN32',
					'_WIN32',
					'_WINDOWS',
				],
			}],
		],	
	
		'configurations': {
            'Debug': {
				'defines': [ 'DEBUG', '_DEBUG' ],
                'msvs_settings': {				
                    'VCCLCompilerTool': {							
						'RuntimeLibrary': '1',
						'WarnAsError': 'true',
						'WarningLevel': '3',
					},						
					'VCLibrarianTool': {						
						'AdditionalDependencies': [
							
						],						
					}
				},
            },
			'Release': {
				'defines': [ 'NDEBUG' ],
                'msvs_settings': {				
                    'VCCLCompilerTool': {							
						'RuntimeLibrary': '0',
						'WarnAsError': 'true',
						'WarningLevel': '3',
					},						
					'VCLibrarianTool': {						
						'AdditionalDependencies': [
							
						],						
					}
				},
            },
		},       
	}
	]
}