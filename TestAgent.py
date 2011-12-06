'''
Created on Nov 25, 2011

@author: tlmaloney
'''
import unittest
import Agent
import Asset as Asset

# Create asset
asset = Asset.make(1, 'Asset')
# Create amount of asset, in this case one unit of asset
amount = 1
# Create two agents
agent1 = Agent.make(1, 'Agent1')
agent2 = Agent.make(2, 'Agent2')

class TestAgent(unittest.TestCase):

    def test_change_asset_ownership(self):
        agent1.change_asset_ownership(asset, amount)
        self.assertEqual(agent1.owned_assets[asset], 1)
    
    def test_change_asset_possession(self):
        agent1.change_asset_possession(asset, amount)
        self.assertEqual(agent1.possessed_assets[asset], 1)

    def test_transfer_ownership(self):
        agent1.transfer_ownership(asset, agent2, amount)
        self.assertEqual(agent2.owned_assets[asset], 1)
        self.assertEqual(agent1.owned_assets[asset], 0)
        
    def test_transfer_possession(self):
        agent1.transfer_possession(asset, agent2, amount)
        self.assertEqual(agent2.possessed_assets[asset], 1)
        self.assertEqual(agent1.possessed_assets[asset], 0)