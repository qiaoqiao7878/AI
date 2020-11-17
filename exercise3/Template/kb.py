from prop_fc import prop_fc
from dpll import fast_dpll
from logic import conjuncts, to_cnf, disjuncts

class FCPropKB:
    def __init__(self):
        self.clauses = set()
    def tell(self, clause):
        self.clauses.add(clause)
    def has_contradicting_knowledge(self):
        dpll_kb = DpllPropKB()
        for prop in self.clauses:
            dpll_kb.tell(prop)
        return dpll_kb.has_contradicting_knowledge()
    def ask(self, clause):
        return prop_fc(self, clause)

class DpllPropKB:
    def __init__(self):
        self.clauses = set()
    def tell(self, sentence):
        self.clauses.update(map(frozenset,
                                map(set,
                                    map(disjuncts,
                                        conjuncts(to_cnf(sentence))))))
    def has_contradicting_knowledge(self):
        return not fast_dpll(self.clauses)
    def ask(self, prop):
        to_prove = frozenset(map(frozenset,
                                 map(set,
                                     map(disjuncts,
                                         conjuncts(to_cnf(~prop)))))) \
                    | self.clauses

        if fast_dpll(to_prove):
            return False
        else:
            self.tell(prop)
            return True
