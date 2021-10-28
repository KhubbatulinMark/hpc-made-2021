import random
import names

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

ranks = [i for i in range(size)]

if rank == 0:
    friends = ['Mark']
    friends.extend([names.get_first_name() for _ in range(size - 1)])
    ranks.remove(rank)
    dest = random.choice(ranks)
    data = {
        'rank': [rank],
        'friends': friends
    }
    comm.send(data, dest=dest)
    print(f"First person at the party {friends[rank]}")

else:
    ranks.remove(rank)
    data = comm.recv()
    print('==>'.join([data['friends'][rank] for rank in data['rank']]))

    for other_rank in data['rank']:
        ranks.remove(other_rank)

    if ranks and len(data) < size - 1:
        dest = random.choice(ranks)
        data['rank'].append(rank)
        comm.send(data, dest=dest)
    else:
        data['rank'].append(rank)
        print('==>'.join([data['friends'][rank] for rank in data['rank']]))
        print(f"{data['friends'][rank]} last at the party")
