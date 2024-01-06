class RuleBasedExpertSystem:
    def __init__(self):
        self.rules = {
            "JK1": ["G1", "G2"],
            "JK2": ["G3", "G4", "G5", "G6", "G7", "G1"],
            "JK3": ["G8", "G9", "G10", "G11"],
        }

        self.symptoms = {
            "JK1": [
                1.7,
                {
                    "G1": 0.9,
                    "G2": 0.8,
                    "G3": 0.6,
                    "G4": 0.8,
                    "G5": 0.6,
                    "G6": 0.3,
                    "G7": 0.5,
                    "G8": 0.7,
                    "G9": 0.7,
                    "G10": 0.7,
                    "G11": 0.6,
                    "G12": 0.9,
                },
            ],
            "JK2": [
                4.1,
                {
                    "G1": 0.7,
                    "G2": 0.6,
                    "G3": 0.7,
                    "G4": 0.6,
                    "G5": 0.7,
                    "G6": 0.8,
                    "G7": 0.6,
                    "G8": 0.5,
                    "G9": 0.9,
                    "G10": 0.3,
                    "G11": 0.6,
                    "G12": 0.7,
                },
            ],
            "JK3": [
                3.1,
                {
                    "G1": 0.6,
                    "G2": 0.9,
                    "G3": 0.7,
                    "G4": 0.9,
                    "G5": 0.5,
                    "G6": 0.7,
                    "G7": 0.9,
                    "G8": 0.9,
                    "G9": 0.6,
                    "G10": 0.8,
                    "G11": 0.8,
                    "G12": 0.9,
                },
            ],
        }

    def diagnose(self, symptoms):
        if len(symptoms) != 0:
            (
                jk1_probability,
                jk2_probability,
                jk3_probability,
            ) = self.calculate_probability(symptoms)

            if jk1_probability > jk2_probability and jk1_probability > jk3_probability:
                return f"Stres Ringan ({jk1_probability})"
            elif (
                jk2_probability > jk1_probability and jk2_probability > jk3_probability
            ):
                return f"Stres Sedang ({jk2_probability})"
            elif (
                jk3_probability > jk1_probability and jk3_probability > jk2_probability
            ):
                return f"Stres Berat ({jk3_probability})"
            else:
                return "Unknown"
        else:
            return "Unknown"

    def calculate_probability(self, inputs):
        # mengecek apakah input ada di rules
        true_values = {
            key: [item in inputs for item in value] for key, value in self.rules.items()
        }

        # menghitung probabilitas penyakit
        bayes_prob = []
        for key, values in true_values.items():
            true_items = [
                item for item, is_true in zip(self.rules[key], values) if is_true
            ]
            p = self.prob(key, true_items)
            bayes_prob.append(p)

        p1 = bayes_prob[0] / sum(bayes_prob)
        p2 = bayes_prob[1] / sum(bayes_prob)
        p3 = bayes_prob[2] / sum(bayes_prob)
        return [p1, p2, p3]

    def prob(self, key, symptoms):
        p = 0
        for symptom in symptoms:
            p += (
                self.symptoms[key][1][symptom] * self.symptoms[key][0]
            ) / self.get_divider(symptom)
        return p

    def get_divider(self, symptom):
        keys_with_input = [key for key, value in self.rules.items() if symptom in value]
        divider = 0
        for key in keys_with_input:
            divider += self.symptoms[key][1][symptom] * self.symptoms[key][0]
        return divider


expert_system = RuleBasedExpertSystem()
symptoms = [
    "G1",
    "G2",
    # "G3",
    # "G4",
    # "G5",
]
diagnosis = expert_system.diagnose(symptoms)

print(f"Diagnosis: {diagnosis}")
