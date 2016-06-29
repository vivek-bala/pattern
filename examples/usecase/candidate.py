from radical.patterns import PoE
from radical.patterns import AppManager
from radical.patterns import Kernel

###################################

# Pipeline of Ensembles

# s1 -  s1 - s1 - s1 - s1 - s1
#                 |
#                s2
#                 |
#     s3 - s3 - s3 - s3


class Workflow(PoE):

	def stage_1(self, instance):

		k = Kernel(name="seq_search")

		return k

	def stage_2(self, instance):

		k = Kernel(name="build_sys")

		return k


	def stage_3(self, instance):

		k = Kernel(name="equil")

		return k

	def stage_4(self, instance):

		k = Kernel(name="prod_md")

		return k

	def stage_5(self, instance):

		k = Kernel(name="struct_ana")

		return k


	def branch_5(self):

		if( int(stage_5["instance_1"].output) > 1):
			# Stable and Convergent
			pass
		else:
			# Can be possibly changed to a function
			self.kill_instances = [1,3,5,7,9]

			self.next_stage = 7

	def stage_6(self, instance):

		k = Kernel(name="mm_pbsa")

		return k

	def branch_6(self):

		if (stage_6["instance_1"].output == "high" ):
			pass
		else:
			# End iterations 
			self.iteration = False

			# Flag to stop execution
			self.next_stage = 0


	def stage_7(self, instance):

		k = Kernel(name="sys_mods")

		self.next_stage = 1
		self.iteration += 1

		return k


if __name__ == '__main__':

	obj = Workflow(ensemble_size= [1, 1, 1, 1000, 1, 1, 1], pipeline_size= 7, iteration = True)

	r_handle = SingleClusterEnvironment(resource="ncsa.bw", #+ other credentials
						)

	app_1 = AppManager(name='heavy_lifting')

	app_1.run(workflow=obj, resource_handle=r_handle)