## Loss Function
* See 'self.__loss' in 'PGPortfolio/pgportfolio/learn/nnagent.py'
* 'self.pv_vector' means immediate reward per time-step.
* 'loss_function6' just computes the average reward per time-step not considering cumulative return.
* In David Silver's class, he pointed that both objective functions follow the Policy Gradient Theorem. It means both are ok.
    * J_avR: average reward per time-step(objective function in this project)
    * J_avV: average value(in continuing environment, e.g. states are continuous)

## Episode
* In this project, episode length is constant and is configured by 'batch_size' parameter.
The only condition with which an episode terminates is that maximum episode length is reached.
* Some other terminating conditions may be considered:
    * Stop loss(止损)
    * Take profit(止盈)
