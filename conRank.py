from typing import List
import corankco as crc

# d = crc.Dataset([
#                 [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12],[13],[14],[15],[16],[17],[18],[19],[20],[21],[22],[23],[24],[25],[26],[27],[28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152]],
#                 [[1],[28],[29],[30],[31],[32],[11],[33],[34],[18],[35],[36],[26],[27],[37],[38],[39],[40],[41],[42],[43],[44],[45],[46],[47],[48],[49],[50],[51],[52],[53],[2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,19,20,21,22,23,24,25,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152]],
#                 [[1],[54],[55],[56],[57],[58],[59],[60],[61],[62],[63],[64],[65],[66],[67],[68],[69],[70],[71],[18],[26],[27],[20],[72],[9],[10],[73],[74],[75],[76],[39],[2,3,4,5,6,7,8,11,12,13,14,15,16,17,19,21,22,23,24,25,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152]],
#                 [[1],[37],[38],[77],[78],[79],[80],[81],[82],[83],[84],[42],[85],[39],[40],[36],[86],[87],[18],[88],[26],[27],[89],[90],[91],[92],[93],[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,28,29,30,31,32,33,34,35,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152]],
#                 [[1],[94],[95],[96],[97],[98],[99],[100],[101],[102],[103],[104],[105],[106],[107],[108],[109],[110],[111],[112],[113],[114],[115],[116],[117],[118],[119],[120],[42],[28],[121],[122],[123],[124],[125],[126],[127],[128],[129],[130],[131],[132],[18],[27],[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,26,29,30,31,32,33,34,35,36,37,38,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,133,134,135,136,137,138,139,140,141,142,143,144,145,146,147,148,149,150,151,152]],
#                 [[1],[37],[38],[42],[86],[87],[133],[134],[135],[136],[137],[138],[139],[140],[141],[142],[18],[35],[26],[27],[2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,19,20,21,22,23,24,25,28,29,30,31,32,33,34,36,39,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,143,144,145,146,147,148,149,150,151,152]],
#                 [[1],[37],[38],[18],[36],[42],[143],[86],[87],[144],[26],[39],[142],[40],[145],[146],[147],[148],[27],[74],[11],[16],[149],[17],[150],[152],[2,3,4,5,6,7,8,9,10,12,13,14,15,19,20,21,22,23,24,25,28,29,30,31,32,33,34,35,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,78,79,80,81,82,83,84,85,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124,125,126,127,128,129,130,131,132,133,134,135,136,137,138,139,140,141]]
#               ])

dataset: crc.Dataset = crc.Dataset.from_raw_list([
[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12]],
[[1],[2],[5],[6],[7],[8],[3],[4],[9],[10],[11],[12]],
[[1],[2],[5],[6],[3],[7],[8],[9],[10],[11],[4,12]],
[[12],[1],[2],[5],[6],[7],[8],[3],[4],[9],[10],[11]],
[[1],[2],[5],[6],[7],[8],[3],[9],[10],[11],[4,12]],
[[1],[2],[5],[6],[3],[4],[7],[8],[10],[9],[11],[12]],
[[1],[2],[5],[6],[3],[7],[8],[9],[10],[11],[4,12]],
[[1],[2],[3],[4],[5],[6],[7],[8],[9],[10],[11],[12]]
                                               ])

sc: crc.ScoringScheme = crc.ScoringScheme([[0., 1., 1., 0., 1., 1.], [1., 1., 0., 1., 1., 0.]])

algorithms_instances: List[crc.RankAggAlgorithm] = [crc.ExactAlgorithm(optimize=False),
                                                 crc.KwikSortRandom(),
                                                 crc.BioConsert(starting_algorithms=None),
                                                 crc.BioConsert(starting_algorithms=[crc.CopelandMethod()]),
                                                 crc.ParCons(bound_for_exact=90, auxiliary_algorithm=crc.BioConsert()),
                                                 crc.CopelandMethod(),
                                                 crc.BioCo(),
                                                 crc.BordaCount(),
                                                 ]

alg2: crc.RankAggAlgorithm = algorithms_instances[2]
alg3: crc.RankAggAlgorithm = algorithms_instances[3]

consensus = alg2.compute_consensus_rankings(dataset=dataset,
                                           scoring_scheme=sc,
                                           return_at_most_one_ranking=False)
f = open("output.txt", "a")
print("consensus", consensus, file=f)
f.close()



#print(consensus.description())