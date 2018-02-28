from local.Bootstrap.compiler_hackathon.classes.Compiler import *

# dsl_file = open('resources_hackathon/eval/ux-design-1.gui')
# dsl_file = open('resources/eval_light/0BA2A4B4-4193-4506-8818-31564225EF8B.gui')
dsl_file = 'resources_hackathon/eval/ux-design-1.gui'

dsl_mapping = "compiler_hackathon/assets/web-dsl-mapping.json"
# dsl_mapping = "compiler/assets/web-dsl-mapping.json"
compiler = Compiler(dsl_mapping)
compiled_website = compiler.compile_dsl(dsl_file)