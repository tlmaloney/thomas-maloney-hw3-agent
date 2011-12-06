'''
Created on Nov 25, 2011

@author: tlmaloney
'''

class Agent(object):
    '''
    An Agent has a name and Unique ID.
    An Agent participates in the Market to trade Assets.
    An Agent keeps track of what Assets s/he owns and in what amounts.
    
    '''

    def __init__(self, unique_id, name, owned_assets={}, possessed_assets={}):
        '''
        Constructor
        
        Keyword arguments:
        unique_id -- Unique ID, integer instance
        name -- the name of the Agent, string instance
        owned_assets -- dictionary of owned assets, keyed by Asset, valued by quantity
        possessed_assets -- dictionary of possessed assets, keyed by Asset, valued by quantity
        '''
        self.unique_id = unique_id
        self.name = name
        self.owned_assets = owned_assets
        self.possessed_assets = possessed_assets

    def __repr__(self):
        """Return a string representation of this class.
        """
        return self.__class__.__name__ + "(" + repr(self.unique_id) + ", " + repr(self.mName) + ")"
    
    def __str__(self):
        """Return a human-friendly string for this class.
        """
        return repr(self) + " " + str(self.mName)
    
    def change_asset_ownership(self, asset, amount):
        """
        Changes quantity of asset in Agent's ownership to 'amount'
        
        Keyword arguments:
        asset -- the asset, Asset instance
        amount -- the amount, instance not specified
        """
        self.owned_assets[asset] = amount
        
    def change_asset_possession(self, asset, amount):
        """
        Changes quantity of asset in Agent's possession to 'amount'
        
        Keyword arguments:
        asset -- the asset, Asset instance
        amount -- the amount, instance not specified
        """
        self.possessed_assets[asset] = amount
    
    def transfer_ownership(self, asset, agent, amount):
        '''
        Transfer ownership of amount of asset from self to agent
        
        Assume self owns enough of the asset to
        cover the amount of asset being transferred
        
        Assume plus/minus operation makes sense for 'amount' instance
        
        Keyword arguments:
        asset -- the asset owned by self, Asset instance
        agent -- the recipient of the asset, Agent instance
        amount -- the amount of asset to be transferred, instance not specified
        '''
        self.owned_assets[asset] -= amount
        if asset not in agent.owned_assets.keys():
            agent.owned_assets[asset] = amount
        else:
            agent.owned_assets[asset] += amount

     
    def transfer_possession(self, asset, agent, amount):
        '''
        Transfer possession of amount of asset from self to agent
        
        Assume self possesses enough of the asset to
        cover the amount of asset being transferred
        
        Assume plus/minus operation makes sense for 'amount' instance
        
        Keyword arguments:
        asset -- the asset owned by self, Asset instance
        agent -- the recipient of the asset, Agent instance
        amount -- the amount of asset to be transferred, instance not specified
        '''
        self.possessed_assets[asset] -= amount
        if asset not in agent.possessed_assets.keys():
            agent.possessed_assets[asset] = amount
        else:
            agent.possessed_assets[asset] += amount


def make(unique_id, name, owned_assets={}, possessed_assets={}):
    '''
    Makes a new Agent instance
    
    Keyword arguments:
    unique_id -- Unique ID, integer instance
    name -- the name of the Agent, string instance
    owned_assets -- dictionary of owned assets, keyed by Asset, valued by quantity
    possessed_assets -- dictionary of possessed assets, keyed by Asset, valued by quantity
    '''
    return Agent(unique_id, name, owned_assets={}, possessed_assets={})